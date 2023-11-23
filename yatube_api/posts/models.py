from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Группы."""

    title = models.CharField(max_length=200, verbose_name="Название группы")
    slug = models.SlugField(unique=True, verbose_name="Слаг группы")
    description = models.TextField(verbose_name="Описание группы")

    class Meta:
        verbose_name_plural = "Группы"
        verbose_name = "Группа"

    def __str__(self):
        return self.title


class Post(models.Model):
    """Посты."""

    text = models.TextField(verbose_name="Содержимое поста")
    pub_date = models.DateTimeField(verbose_name="Дата публикации",
                                    auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts",
        verbose_name="Автор поста"
    )
    image = models.ImageField(
        upload_to="posts/", null=True, blank=True, verbose_name="Изображение"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name="Группа",
    )

    class Meta:
        verbose_name_plural = "Посты"
        verbose_name = "Пост"

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Комментарии."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор поста",
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments",
        verbose_name="Пост"
    )
    text = models.TextField(verbose_name="Содержимое комментария")
    created = models.DateTimeField(
        verbose_name="Дата добавления", auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"

    def __str__(self):
        return self.text
