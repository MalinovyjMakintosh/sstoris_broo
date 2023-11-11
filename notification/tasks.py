from celery import shared_task
from django.core.mail import send_mail
from vk_api import VkApi, VkApiResponseException
from django.contrib.auth.models import User

@shared_task
def send_notification(user_id, message):
    try:
        # VK API 
        vk_session = VkApi(token='YOUR_GROUP_ACCESS_TOKEN')
        vk = vk_session.get_api()
        vk.messages.send(
            user_id=user_id,
            message=message,
            random_id=0  
        )

        #  email notification
        send_mail(
            'Notification',
            message,
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        #  user profile with the notification
        try:
            user = User.objects.get(id=user_id)
            user.profile.notification = message
            user.profile.save()
            print(f"Профиль пользователя {user.username} успешно обновлен с уведомлением: {message}")
        except User.DoesNotExist:
            print(f"Пользователь с id={user_id} не найден.")
        except Exception as e:
            print(f"Ошибка при обновлении профиля пользователя: {e}")

    except VkApiResponseException as e:
        print(f"VK API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
