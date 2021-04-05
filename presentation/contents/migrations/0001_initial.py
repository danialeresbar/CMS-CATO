# Generated by Django 2.2.3 on 2020-07-24 23:07

import ckeditor.fields
import colorfield.fields
from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
        ('menus', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('title', models.CharField(default='Banners gallery', max_length=200, verbose_name="Banner's gallery title")),
                ('slug_banner_gallery', models.SlugField(default='-', verbose_name='Slug')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bannergallery_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bannergallery_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Banners gallery',
                'verbose_name_plural': 'Banners galleries',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='ComponentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.CharField(max_length=35, verbose_name='Component name')),
                ('component_nickname', models.CharField(blank=True, max_length=35, null=True, verbose_name='Component nickname')),
            ],
            options={
                'verbose_name': 'Component type',
                'verbose_name_plural': 'Components type',
                'unique_together': {('component_name', 'component_nickname')},
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('contact_title', models.CharField(default='Contact', max_length=100, null=True, verbose_name='Contact title')),
                ('background', models.ImageField(blank=True, null=True, upload_to='Contents/contacts/background', verbose_name='Background form image')),
                ('slug_contact', models.SlugField(default='-', verbose_name='Slug')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='GallerySelector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('banner_gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.BannerGallery', verbose_name='Select banners galleries')),
            ],
            options={
                'verbose_name': 'Banners gallery',
                'verbose_name_plural': 'Banners galleries',
                'ordering': ['-active'],
            },
        ),
        migrations.CreateModel(
            name='GeneralData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('title_one', models.CharField(default='General Data', max_length=100, verbose_name='Title')),
                ('logo_site', models.ImageField(blank=True, null=True, upload_to='Tools/logos', verbose_name='Logo')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('slug_general_data', models.SlugField(default='-', verbose_name='Slug')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='generaldata_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='generaldata_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'General data',
                'verbose_name_plural': 'General data',
                'ordering': ['-active', 'creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=128, verbose_name="Menu's name")),
                ('general', models.BooleanField(default=False, verbose_name='Menú general')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('page_type', models.CharField(choices=[('MAKING', 'Construcción'), ('CONTENT', 'Contenido')], default='MAKING', max_length=20, verbose_name="Page's type")),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Title')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('slug_page', models.SlugField(default='-', verbose_name='Slug')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('gallery_selector', models.ManyToManyField(blank=True, through='contents.GallerySelector', to='contents.BannerGallery', verbose_name='Select banners galleries')),
                ('inner_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.Menu', verbose_name='Menu')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.Page', verbose_name="Page's parent")),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Page',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('title_post', models.CharField(max_length=50, verbose_name="Post's title")),
                ('logo', models.ImageField(blank=True, upload_to='Contents/banners//animated_logos', verbose_name="Post's image")),
                ('icon', models.ImageField(blank=True, upload_to='Contents/banners//icon_post', verbose_name="Post's icon")),
                ('external_url', models.URLField(blank=True, null=True, verbose_name='URL externa')),
                ('slug_post', models.SlugField(default='-')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.Post', verbose_name="Post's parent")),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name="Section's title")),
                ('background', models.ImageField(blank=True, null=True, upload_to='Contents/sections/background', verbose_name='Background image')),
                ('background_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18, verbose_name="Section's background color")),
                ('align', models.CharField(choices=[('RIGHT', 'Right'), ('LEFT', 'Left'), ('RIGHT_LEFT', 'Right - left'), ('LEFT_RIGHT', 'left - right')], default='RIGHT', max_length=20, verbose_name='Posts texts alignment')),
                ('slug_section', models.SlugField(default='-', verbose_name='Slug')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('lines_to_show', models.SmallIntegerField(default=1, help_text='Between one and four lines', verbose_name='Display this many lines before show more')),
                ('title_visibility', models.BooleanField(default=True, verbose_name='Title visibility')),
                ('subtitle_visibility', models.BooleanField(default=False, verbose_name='Subtitle visibility')),
                ('logo_visibility', models.PositiveSmallIntegerField(choices=[(1, 'Above title'), (2, 'To the left of the title'), (3, 'To the left of the post'), (4, 'as background'), (5, 'No visible')], default=3, verbose_name='Image visibility')),
                ('tag_visibility', models.BooleanField(default=False, verbose_name='Tags visibility')),
                ('description_visibility', models.BooleanField(default=False, verbose_name='Description visibility')),
                ('gallery_visibility', models.BooleanField(default=False, verbose_name='Gallery visibility')),
                ('component_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.ComponentType', verbose_name='Posts visualization component')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tag name')),
                ('slug_tag', models.SlugField(default='-', verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('name', models.CharField(max_length=50, verbose_name='Social network name')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='Tools/Logo_social', verbose_name='Icon')),
                ('icon_css', models.CharField(blank=True, max_length=50, null=True, verbose_name='Icon css')),
                ('url', url_or_relative_url_field.fields.URLOrRelativeURLField(verbose_name='link social')),
                ('slug', models.SlugField(default='-', verbose_name='Slug')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socialnetwork_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('general_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contents.GeneralData', verbose_name='Footer')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socialnetwork_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Social network',
                'verbose_name_plural': 'Social networks',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SectionSelector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sectionselector_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contents.Page', verbose_name="Page's section")),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contents.Section', verbose_name='Section')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sectionselector_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Select sections',
                'verbose_name_plural': 'Select sections',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='section',
            name='page',
            field=models.ManyToManyField(blank=True, through='contents.SectionSelector', to='contents.Page', verbose_name="Page's section"),
        ),
        migrations.AddField(
            model_name='section',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.CreateModel(
            name='PostSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_family', models.BooleanField(default=False, help_text="Check the box if you want the post's family to shown in the section", verbose_name='Show family')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.Post', verbose_name="Section's posts")),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.Section', verbose_name='Section')),
            ],
            options={
                'verbose_name': 'Post settings',
                'verbose_name_plural': 'Order posts',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='PostGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Image name in spanish')),
                ('title_translation', models.CharField(max_length=100, null=True, verbose_name='Image name in english')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Contents/Post_gallery_images', verbose_name='Load image')),
                ('image_360', models.BooleanField(blank=True, default=False, help_text='Check the box if is a 360 image', verbose_name='is it a 360 image?')),
                ('url_youtube', models.CharField(blank=True, max_length=255, null=True, verbose_name='Youtube video url')),
                ('order', models.SmallIntegerField(default=0)),
                ('slug_post_gallery', models.SlugField(default='-', verbose_name='Slug')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postgallery_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.Post', verbose_name='Post')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postgallery_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ManyToManyField(through='contents.PostSettings', to='contents.Section', verbose_name='Sections'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.CreateModel(
            name='PartnersGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('image', models.ImageField(upload_to='Contents/partner_images', verbose_name='Institution image')),
                ('url', models.URLField(blank=True, default=None, null=True, verbose_name='Institution url')),
                ('order', models.SmallIntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partnersgallery_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.GeneralData', verbose_name='General data')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partnersgallery_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Institutional links',
                'verbose_name_plural': 'Institutional links',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=128, verbose_name="Menu's item name")),
                ('url', models.URLField(blank=True, max_length=256, null=True, verbose_name='External url')),
                ('slug_url', models.CharField(blank=True, max_length=50, null=True, verbose_name='URL Slug')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuitem_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='contents.Menu', verbose_name='Menu')),
                ('page_url', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.Page', verbose_name='Page url')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='contents.MenuItem', verbose_name="Menu's item parent")),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuitem_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': "Menu's item",
            },
        ),
        migrations.AddField(
            model_name='galleryselector',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contents.Page', verbose_name='Show banner gallery in this page'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('title', models.CharField(max_length=200, verbose_name="Banner's title")),
                ('image', models.ImageField(blank=True, null=True, upload_to='Contents/banners/', verbose_name='Background image')),
                ('image_360', models.BooleanField(blank=True, default=False, help_text='Check the box if is a 360 image', verbose_name='is it a 360 image?')),
                ('animated_logo', models.ImageField(blank=True, null=True, upload_to='Contents/banners//animated_logos', verbose_name='animated logo')),
                ('button_link', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, default=None, null=True, verbose_name='Add link to banner')),
                ('icon_css_banner', models.CharField(blank=True, default=None, help_text='Lista de Íconos: <a href=https://fontawesome.com/v4.7.0/icons/ target=_blank> https://fontawesome.com/v4.7.0/icons/ </a>', max_length=20, null=True, verbose_name='icon css button banner')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('url_youtube', models.CharField(blank=True, max_length=255, null=True, verbose_name='Youtube video url')),
                ('slug_banner', models.SlugField(default='-', verbose_name='Slug')),
                ('banner_gallery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.BannerGallery', verbose_name='Banners gallery')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SectionLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name="Section's title")),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name="Section's description")),
                ('sect_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='Json content')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Language')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_lang', to='contents.Section', verbose_name='Section')),
            ],
            options={
                'verbose_name': "Section's language",
                'verbose_name_plural': "Section's languages",
                'unique_together': {('language', 'section')},
            },
        ),
        migrations.CreateModel(
            name='PostLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.CharField(blank=True, max_length=50, null=True, verbose_name="Post's title")),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True, verbose_name="Post's subtitle")),
                ('long_description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Post's description text")),
                ('post_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='Json content')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Language')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_lang', to='contents.Post', verbose_name='Post')),
                ('tag', models.ManyToManyField(blank=True, to='contents.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Post language',
                'verbose_name_plural': 'Post languages',
                'ordering': ['post'],
                'unique_together': {('language', 'post')},
            },
        ),
        migrations.CreateModel(
            name='PageLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name="Page's title")),
                ('description', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name="Page's description")),
                ('page_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, verbose_name='Json content')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Language')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_lang', to='contents.Page', verbose_name='Page')),
            ],
            options={
                'verbose_name': 'Page language',
                'verbose_name_plural': 'Page languages',
                'unique_together': {('language', 'page')},
            },
        ),
        migrations.CreateModel(
            name='MenuLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='Json content')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Language')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_lang', to='contents.Menu')),
            ],
            options={
                'verbose_name': "Menu's language",
                'unique_together': {('language', 'menu')},
            },
        ),
        migrations.CreateModel(
            name='MenuItemLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name="Menu's name")),
                ('menu_item_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='Json content')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Language')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_lang', to='contents.MenuItem')),
            ],
            options={
                'verbose_name': "Menu's item language",
                'unique_together': {('language', 'menu_item')},
            },
        ),
        migrations.CreateModel(
            name='GeneralDataLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_one', models.CharField(blank=True, max_length=100, null=True, verbose_name='footer title one')),
                ('about', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Footer description')),
                ('title_two', models.CharField(blank=True, max_length=100, null=True, verbose_name='footer title two')),
                ('general_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='Json content')),
                ('general_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='general_data_lang', to='contents.GeneralData', verbose_name='General data')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'General data language',
                'verbose_name_plural': 'General data languages',
                'unique_together': {('language', 'general_data')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='galleryselector',
            unique_together={('page', 'banner_gallery')},
        ),
        migrations.CreateModel(
            name='ContactLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Contact description')),
                ('title_form', models.CharField(default='', max_length=50, verbose_name='Title form contact')),
                ('subtitle_form', models.CharField(default='', max_length=50, verbose_name='Subtitle form contact')),
                ('name_form', models.CharField(default='', max_length=50, verbose_name='Name form contact')),
                ('mail_form', models.CharField(default='', max_length=50, verbose_name='Mail form contact')),
                ('subject_form', models.CharField(default='', max_length=50, verbose_name='Affair form contact')),
                ('body_form', models.TextField(default='', verbose_name='Body form contact')),
                ('text_button', models.CharField(default='', max_length=50, verbose_name='Text button form contact')),
                ('contact_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='Json content')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_lang', to='contents.Contact', verbose_name='Contact')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'unique_together': {('language', 'contact')},
            },
        ),
        migrations.CreateModel(
            name='BannerLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name="Banner's title")),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True, verbose_name="Banner's subtitle")),
                ('banner_description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Banner's description text")),
                ('button_text', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='text button banner')),
                ('banner_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='Json content')),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banner_lang', to='contents.Banner', verbose_name='banner')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Language')),
            ],
            options={
                'verbose_name': "Banner's language",
                'verbose_name_plural': "Banner's laguages",
                'unique_together': {('language', 'banner')},
            },
        ),
    ]