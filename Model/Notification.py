class Notification(models.Model):
    user = models.name = models.ForeignKey(User, on_delete=models.CASCADE)
    connect_token = models.CharField(max_lenth=64, null=True)