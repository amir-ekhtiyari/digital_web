from django.db import models


class Image(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="محصول",
    )
    image = models.ImageField(upload_to="images/")
    caption = models.CharField(max_length=100, blank=True, verbose_name="عنوان")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.product_id} - {self.id}"
