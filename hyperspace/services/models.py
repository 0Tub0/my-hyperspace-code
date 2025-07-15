from django.db import models
from django.utils.text import slugify  # Import slugify for generating slugs

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=100) #title: Modelin (örneğin bir kitap, makale, görev vs.) başlığını tutacak alanın ismidir. models.CharField: Django’daki kısa metin (string) tutmak için kullanılan bir alan tipidir.
    description=models.TextField() #description: Modelin açıklamasını tutacak alanın ismidir. models.TextField: Django’daki uzun metin (string) tutmak için kullanılan bir alan tipidir.
    icon_class=models.CharField(max_length=50) #icon_class: Modelin simgesini tutacak alanın ismidir. models.CharField: Django’daki kısa metin (string) tutmak için kullanılan bir alan tipidir.
    is_featured=models.BooleanField(default=False) #is_featured: Modelin öne çıkarılıp çıkarılmayacağını tutacak alanın ismidir. models.BooleanField: Django’daki boolean (True/False) değer tutmak için kullanılan bir alan tipidir. default=False: Varsayılan değeri False olarak ayarlar, yani öne çıkarılmamış olarak başlar.
    slug=models.SlugField(unique=True, blank=True) #slug: Modelin URL dostu bir tanımlayıcısını tutacak alanın ismidir. models.SlugField: Django’daki URL dostu bir metin (string) tutmak için kullanılan bir alan tipidir.

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']  # Modelin sıralama düzenini belirler, burada başlığa göre artan sırada sıralanır.
        verbose_name = 'Service'
        verbose_name_plural = 'Services'