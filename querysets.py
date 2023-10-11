filtered_posts = Post.objects.filter(date__range = ["2011-01-01", timezone.now()], body_text__icontains='Music')

april_filt_posts = Post.objects.filter(pub_date__month = 4)

name_filt_posts = Post.objects.filter(blog__name = "Technology") 

last_ten_posts = Post.objects.all().order_by('-pk')[:10]

comment_filt_posts = Post.objects.get(blog__name="Art").filter(comments__count__gte = 15)