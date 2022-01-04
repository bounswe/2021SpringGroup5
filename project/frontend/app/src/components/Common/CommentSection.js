import { Avatar, Button, TextField } from '@mui/material';
import { Controller, useForm } from 'react-hook-form';
import { useMutation, useQueryClient } from 'react-query';
import { postComment } from '../../services/EventService';
import '../../screens/CommentSection.css';

function CommentSection({ comments, event_id }) {
  const { handleSubmit, control } = useForm();
  const queryClient = useQueryClient();
  const mutation = useMutation('comment', text => postComment(event_id, text), {
    onSuccess: () => {
      queryClient.invalidateQueries(`eventDetail/${event_id}`).then();
    },
  });

  const onSubmit = data => {
    mutation.mutate(data.text);
  };
  return (
    <div className="comment-form event-comment">
      {comments.map((comment, index) => {
        return (
          <div className="comment-info" key={index} data-testId={'comment_'.concat(index)}>
            <Avatar alt={comment.username} src={comment.image_url} />
            <div>
              <h4 style={{ margin: 0, textAlign: 'left' }}>{comment.username}</h4>
              <p style={{ textAlign: 'left' }}>{comment.content}</p>
              <p style={{ textAlign: 'left', color: 'gray' }}>{comment.created_date}</p>
            </div>
          </div>
        );
      })}
      <h4>Leave a Comment</h4>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Controller
          name="text"
          control={control}
          render={({ field }) => (
            <TextField
              data-testId="comment-area"
              fullWidth={true}
              multiline={true}
              maxRows="5"
              placeholder="Leave a comment"
              {...field}
            />
          )}
        />

        <Button className="comment-button" color="success" variant="outlined" type="submit">
          Submit
        </Button>
      </form>
    </div>
  );
}
export default CommentSection;

export function EquipmentCommentSection({ comments, equipment_id }) {
  const { handleSubmit, control } = useForm();
  const queryClient = useQueryClient();
  const mutation = useMutation('comment', text => postComment(equipment_id, text), {
    onSuccess: () => {
      queryClient.invalidateQueries(`equipmentDetail/${equipment_id}`).then();
    },
  });

  const onSubmit = data => {
    mutation.mutate(data.text);
  };
  return (
    <div className="comment-form event-comment">
      {comments.map((comment, index) => {
        return (
          <div className="comment-info" key={index} data-testId={'comment_'.concat(index)}>
            <Avatar alt={comment.username} src={comment.image_url} />
            <div>
              <h4 style={{ margin: 0, textAlign: 'left' }}>{comment.username}</h4>
              <p style={{ textAlign: 'left' }}>{comment.content}</p>
              <p style={{ textAlign: 'left', color: 'gray' }}>{comment.created_date}</p>
            </div>
          </div>
        );
      })}
      <h4>Leave a Comment</h4>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Controller
          name="text"
          control={control}
          render={({ field }) => (
            <TextField
              data-testId="comment-area"
              fullWidth={true}
              multiline={true}
              maxRows="5"
              placeholder="Leave a comment"
              {...field}
            />
          )}
        />

        <Button className="comment-button" color="success" variant="outlined" type="submit">
          Submit
        </Button>
      </form>
    </div>
  );
}
