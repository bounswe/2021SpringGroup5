import { httpClient } from '../httpClient';

export function getEvent(me, event_id) {

  return httpClient
    .post(`/post/get_event_post_details/`, {
      '@context': 'https://www.w3.org/ns/activitystreams',
      summary: `${me.name} is reading an event post.`,
      type: 'View',

      actor: {
        type: 'Person',
        name: `${me.name}`,
        surname: `${me.surname}`,
        username: `${me.username}`,
        Id: Number.parseInt(me.Id),
      },

      object: {
        type: 'EventPost',
        post_id: Number.parseInt(event_id),
      },

    })
    .then(res => res.data);

}

export function getEquipment(me, eq_id) {

  return httpClient
    .post(`/post/get_equipment_post_details/`, {
      '@context': 'https://www.w3.org/ns/activitystreams',
      summary: `${me.name} is reading an event post.`,
      type: 'View',

      actor: {
        type: 'Person',
        name: `${me.name}`,
        surname: `${me.surname}`,
        username: `${me.username}`,
        Id: Number.parseInt(me.Id),
      },

      object: {
        type: 'EquipmetPost',
        post_id: Number.parseInt(eq_id),
      },

    })
    .then(res => res.data);

}

export function postComment(post_id, text) {
  return httpClient.post(`post/create_event_comment/`, {
    '@context': 'https://www.w3.org/ns/activitystreams',
    summary: '',
    type: 'Create',
    object: {
      type: 'Comment',
      content: text,
      post_id: post_id,
    },
  });
}

export function acceptUser(me, event_id, user_id) {
  return httpClient.post(`/post/accept_application/`, {
    '@context': 'https://www.w3.org/ns/activitystreams',
    summary: `${me.name} accepted an application`,
    type: 'Accept',
    applicant: {
      Id: user_id,
    },
    object: {
      type: 'EventPost',
      Id: event_id,
    },
  });
}

export function rejectUser(me, event_id, user_id) {
  return httpClient.post(`/post/reject_application/`, {
    '@context': 'https://www.w3.org/ns/activitystreams',
    summary: `${me.name} rejected an application`,
    type: 'Reject',
    applicant: {
      Id: user_id,
    },
    object: {
      type: 'EventPost',
      Id: event_id,
    },
  });
}

export function applyEvent(me, event_id) {
  return httpClient.post(`/post/apply_to_event/`, {
    '@context': 'https://www.w3.org/ns/activitystreams',
    summary: `${me.name} rejected an application`,
    type: 'Application',
    object: {
      type: 'EventPost',
      Id: event_id,
    },
  });
}
