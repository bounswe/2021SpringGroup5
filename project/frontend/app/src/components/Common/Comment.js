function Comment() {
    return (
    <div className="comment-form event-comment">
    <h4>Leave a Comment</h4>
    <form id="contact-form" method="POST">
        <div className="row">
            <div className="col-md-6">
                <div className="form-group">
                    <input name="Name" id="name" placeholder="Name *" className="form-control" type="text" />
                </div>
            </div>
            <div className="col-md-6">
                <div className="form-group">
                    <input name="Email" id="email" placeholder="Email *" className="form-control" type="email" />
                </div>
            </div>
            <div className="col-md-12">
                <div className="form-group">
                    <textarea name="message" id="message" placeholder="Your message *" rows="4" className="form-control"></textarea>
                </div>
            </div>
            <div className="col-md-12">
                <div className="send">
                    <button className="px-btn theme"><span>Submit</span> <i className="arrow"></i></button>
                </div>
            </div>
        </div>
    </form>
    </div>
    )
}
export default Comment;
