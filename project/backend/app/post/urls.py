from django.urls import path
from . import views

urlpatterns=[
    path('create_event_post/',views.createEventPost,name='create an event post'),
    path('create_equipment_post/',views.createEquipmentPost,name='create an equipment post'),
    path('delete_event_post/',views.deleteEventPost,name='delete an event post'),
    path('delete_equipment_post/',views.deleteEquipmentPost,name='delete an equipment post'),
    path('change_equipment_post/',views.changeEquipmentInfo,name='update equipment post information'),
    path('change_event_post/',views.changeEventInfo,name='update event post information'),
    path('postpone_event/',views.postponeEvent,name='postpone an event'),
    path('get_event_post_details/',views.getEventPostDetails,name='get event post details'),
    path('create_event_comment/',views.createEventComment,name='create a comment'),
    path('create_equipment_comment/', views.createEquipmentComment, name='create a comment'),
    path('get_waiting_applications/',views.getWaitingApplications,name='get waiting applications'),
    path('get_rejected_applications/',views.getRejectedApplications,name='get rejected applications'),
    path('get_accepted_applications/',views.getAcceptedApplications,name='get accepted applications'),
    path('get_inadequate_applications/',views.getInadequateApplications,name='get inadequate applications'),
    path('get_equipment_post_details/',views.getEquipmentPostDetails,name='get equipment post details'),
    path('save_sports/',views.SaveSportListScript.as_view(),
         name="save sports"),
    path('save_skill_levels/',views.SaveSkillLevelsScript.as_view(),name='save skill levels'),
    path('save_badges/',views.SaveBadgesScript.as_view(),name='save badges'),
    path('apply_to_event/',views.applyToEvent,name='creates an application to event'),
    path('spectate_to_event/',views.spectateToEvent,name='spectate to event'),
    path('get_spectators/',views.getSpectators,name='get spectators of an event'),
    path('accept_application/',views.acceptApplicant,name='accept an application'),
    path('reject_application/',views.rejectApplicant,name='reject an application'),
    path('get_event_post_analytics/',views.getEventPostAnalytics,name='get event post analytics'),
    path('get_all_badges/', views.getAllBadges, name='get All Badges'),
    path('send_badge/', views.sendBadge, name='Send Badge'),


]