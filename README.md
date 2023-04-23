# Django-REST-framework-sample

Django REST framework のチュートリアルをやっていく

## 開発環境

### コンテナ起動 (`api`と`postgresql`)

```bash
docker-compose up
```

### マイグレ

1. 起動中にコンテナに入る

   ```bash
   docker exec -it sample_django_rest_container bash
   ```

2. マイグレファイル作成

   ```bash
   python manage.py makemigrations
   ```

3. DB に反映

   ```bash
   python manage.py migrate
   ```

## チュートリアル

- [x] https://www.django-rest-framework.org/tutorial/1-serialization/
- [x] https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
- [x] https://www.django-rest-framework.org/tutorial/3-class-based-views/
- [x] https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
- [x] https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
- [x] https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
