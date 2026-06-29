from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Course, Enrollment, Lesson, LessonProgress


def get_course_lessons(course):
    return Lesson.objects.filter(module__course=course).order_by(
        "module_id",
        "id",
    )


def get_completed_lesson_ids(user, course=None):
    queryset = LessonProgress.objects.filter(user=user, completed=True)

    if course is not None:
        queryset = queryset.filter(lesson__module__course=course)

    return set(queryset.values_list("lesson_id", flat=True))


def build_course_progress(user, course):
    lessons = get_course_lessons(course)
    total_lessons = lessons.count()

    completed_lesson_ids = set()
    completed_lessons = 0
    progress_percent = 0
    is_enrolled = False
    is_completed = False
    next_lesson = None

    if user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(
            user=user,
            course=course,
        ).exists()
        completed_lesson_ids = get_completed_lesson_ids(user, course)
        completed_lessons = len(completed_lesson_ids)

        if total_lessons > 0:
            progress_percent = int(
                (completed_lessons / total_lessons) * 100
            )

        is_completed = (
            total_lessons > 0
            and completed_lessons == total_lessons
        )

        for lesson in lessons:
            if lesson.id not in completed_lesson_ids:
                next_lesson = lesson
                break

    return {
        "lessons": lessons,
        "total_lessons": total_lessons,
        "completed_lesson_ids": completed_lesson_ids,
        "completed_lessons": completed_lessons,
        "progress_percent": progress_percent,
        "is_enrolled": is_enrolled,
        "is_completed": is_completed,
        "next_lesson": next_lesson,
    }


def course_list(request):
    courses = Course.objects.all()
    course_progress = {}

    if request.user.is_authenticated:
        for course in courses:
            progress = build_course_progress(request.user, course)
            course_progress[course.id] = {
                "is_enrolled": progress["is_enrolled"],
                "total_lessons": progress["total_lessons"],
                "completed_lessons": progress["completed_lessons"],
                "progress_percent": progress["progress_percent"],
                "is_completed": progress["is_completed"],
                "next_lesson": progress["next_lesson"],
            }

    context = {
        "courses": courses,
        "course_progress": course_progress,
    }
    return render(request, "courses/course_list.html", context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    modules = course.module_set.all()
    progress = build_course_progress(request.user, course)

    context = {
        "course": course,
        "modules": modules,
        "is_enrolled": progress["is_enrolled"],
        "completed_lesson_ids": progress["completed_lesson_ids"],
        "total_lessons": progress["total_lessons"],
        "completed_lessons": progress["completed_lessons"],
        "progress_percent": progress["progress_percent"],
        "is_completed": progress["is_completed"],
        "next_lesson": progress["next_lesson"],
    }
    return render(request, "courses/course_detail.html", context)


@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course = lesson.module.course

    is_enrolled = Enrollment.objects.filter(
        user=request.user,
        course=course,
    ).exists()

    if not is_enrolled:
        return redirect("courses:course_detail", pk=course.pk)

    completed = LessonProgress.objects.filter(
        user=request.user,
        lesson=lesson,
        completed=True,
    ).exists()

    progress = build_course_progress(request.user, course)

    context = {
        "lesson": lesson,
        "completed": completed,
        "is_enrolled": is_enrolled,
        "course": course,
        "course_progress_percent": progress["progress_percent"],
        "course_completed_lessons": progress["completed_lessons"],
        "course_total_lessons": progress["total_lessons"],
        "course_is_completed": progress["is_completed"],
        "next_lesson": progress["next_lesson"],
    }
    return render(request, "courses/lesson_detail.html", context)


@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course,
    )

    return redirect("courses:course_detail", pk=course.pk)


@login_required
def complete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course = lesson.module.course

    enrollment_exists = Enrollment.objects.filter(
        user=request.user,
        course=course,
    ).exists()

    if not enrollment_exists:
        return redirect("courses:course_detail", pk=course.pk)

    progress, created = LessonProgress.objects.get_or_create(
        user=request.user,
        lesson=lesson,
        defaults={"completed": True},
    )

    if not created and not progress.completed:
        progress.completed = True
        progress.save()

    course_progress = build_course_progress(request.user, course)

    if course_progress["is_completed"]:
        return redirect("courses:course_certificate", pk=course.pk)

    return redirect("courses:continue_course", pk=course.pk)


@login_required
def continue_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    is_enrolled = Enrollment.objects.filter(
        user=request.user,
        course=course,
    ).exists()

    if not is_enrolled:
        return redirect("courses:course_detail", pk=course.pk)

    progress = build_course_progress(request.user, course)

    if progress["next_lesson"]:
        return redirect(
            "courses:lesson_detail",
            pk=progress["next_lesson"].pk,
        )

    return redirect("courses:course_certificate", pk=course.pk)


@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(
        user=request.user,
    ).select_related("course")
    enrolled_courses = [enrollment.course for enrollment in enrollments]

    my_courses_data = []

    for course in enrolled_courses:
        progress = build_course_progress(request.user, course)

        my_courses_data.append({
            "course": course,
            "total_lessons": progress["total_lessons"],
            "completed_lessons": progress["completed_lessons"],
            "progress_percent": progress["progress_percent"],
            "is_completed": progress["is_completed"],
            "next_lesson": progress["next_lesson"],
        })

    context = {
        "my_courses_data": my_courses_data,
    }
    return render(request, "courses/my_courses.html", context)


@login_required
def course_certificate(request, pk):
    course = get_object_or_404(Course, pk=pk)

    is_enrolled = Enrollment.objects.filter(
        user=request.user,
        course=course,
    ).exists()

    if not is_enrolled:
        return redirect("courses:course_detail", pk=course.pk)

    progress = build_course_progress(request.user, course)

    if not progress["is_completed"]:
        return redirect("courses:course_detail", pk=course.pk)

    context = {
        "course": course,
        "progress_percent": progress["progress_percent"],
        "completed_lessons": progress["completed_lessons"],
        "total_lessons": progress["total_lessons"],
    }
    return render(request, "courses/course_certificate.html", context)