from django.contrib import admin

from .models import Category, Product, Order, Feedback


class ProductTabularInline(admin.TabularInline):
    model = Product


class AppAdminSite(admin.AdminSite):
    site_header = 'SITE HEADER'
    site_title = 'TITLE'
    index_title = 'INDEX TITLE'


appadmin = AppAdminSite(name='appadmin')


@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'Н/У'
    actions = (make_published, make_unpublished)
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'Введите имя род. категории или id категории'
    inlines = (ProductTabularInline, )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'Н/У'
    actions = (make_published, make_unpublished)
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = 'заголов/id/артикль/цена'
    fieldsets = (
        ('Основные настройки', {
            'fields': ('title', 'article', 'price', 'category'),
            'description': 'описание'
        }),
        ('Дополнительные настройки', {
            'fields': ('is_published', 'descr', 'count', 'image')
        })
    )
    list_editable = ('category', )
    prepopulated_fields = {'descr': ('title', 'article')}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'date_created', 'is_paid')
    list_filter = ('is_paid', )
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created', )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'date_created')
    list_filter = ('email', 'phone_number')
    date_hierarchy = 'date_created'


class FeedbackManager(FeedbackAdmin):
    readonly_fields = ('date_created', 'email', 'phone_number', 'message', 'name')


appadmin.register(Category, CategoryAdmin)
appadmin.register(Product, ProductAdmin)
appadmin.register(Order, OrderAdmin)
appadmin.register(Feedback, FeedbackManager)
