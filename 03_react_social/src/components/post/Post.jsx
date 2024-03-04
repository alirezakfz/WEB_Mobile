import React from 'react'
import './post.css'
import { MoreVert } from '@mui/icons-material'
import { Users } from '../../dummyData'

export default function Post({post}) {
    const[like, setLike] = React.useState(post.like)
    const[isLiked, setIsLiked] = React.useState(false)

    const likeHandler =()=>{
        setLike(state => isLiked ? state-1 : state+1)
        setIsLiked(prevState => !prevState)
    }

  return (
    <div className="post">
        <div className="postWrapper">
            <div className="postTop">

                <div className="postTopLeft">
                    <img className='postProfileImg' 
                        src={Users.filter((u) => u.id===post.userId)[0].profilePicture}
                        alt='' />
                    <span className="postUsername">
                        {Users.filter((u) => u.id===post.userId)[0].username}
                        </span>
                    <span className="postDate">{post.date}</span>
                </div>
                    
                <div className="postTopRight">
                    <MoreVert />
                </div>
            </div>
            
            <div className="postCenter">
                <span className="postText">{post?.desc} </span>
                <img className='postImg' src={post.photo} alt='' />
            </div>
            <div className="postButtom">
                <div className="postButtomLeft">
                    <img  className='likeIcon' src='/assets/like.png' onClick={likeHandler}/>
                    <img className='likeIcon' src='/assets/heart.png' onClick={likeHandler}/>
                    <span className="postLikeCouner">{like} people like it.</span>
                </div>
                <div className="postButtomRight">
                    <span className="postCommentText">
                        {post.comment} comments
                    </span>
                </div>
            </div>
        </div>
    </div>
  )
}
