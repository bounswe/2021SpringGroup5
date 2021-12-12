from django.urls import path
from post import views

urlpatterns=[
    path('create_event_post/',views.createEventPost,name='create an event post'),
    path('create_equipment_post/',views.createEquipmentPost,name='create an equipment post'),
    path('delete_event_post/',views.deleteEventPost,name='delete an event post'),
    path('delete_equipment_post/',views.deleteEquipmentPost,name='delete an equipment post'),
    path('change_equipment_post/',views.changeEquipmentInfo,name='update equipment post information'),
    path('change_event_post/',views.changeEventInfo,name='update event post information'),
    path('get_event_post_details/',views.getEventPostDetails,name='get event post details'),
    path('get_equipment_post_details/',views.getEquipmentPostDetails,name='get equipment post details'),
    path('save_sports/',views.SaveSportListScript.as_view(),
         name="save sports"),
    path('save_skill_levels/',views.SaveSkillLevelsScript.as_view(),name='save skill levels'),
    path('save_badges/',views.SaveBadgesScript.as_view(),name='save badges'),
    path('apply_to_event/',views.applyToEvent,name='creates an application to event'),
    path('accept_application/',views.acceptApplicant,name='accept an application'),
]