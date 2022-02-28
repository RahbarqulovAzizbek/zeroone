# Generated by Django 4.0.2 on 2022-02-18 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('avatar', models.ImageField(upload_to='author-avatars/', verbose_name='avatar')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='BlogPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('main_image', models.ImageField(upload_to='blog-post-img/', verbose_name='main image')),
                ('banner', models.ImageField(upload_to='blog-post-img/', verbose_name='banner')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='posts', to='blog.authormodel', verbose_name='author')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
        migrations.CreateModel(
            name='BlogTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('comment', models.TextField(verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogpostmodel', verbose_name='post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.AddField(
            model_name='blogpostmodel',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='blog.BlogTagModel', verbose_name='tags'),
        ),
    ]
