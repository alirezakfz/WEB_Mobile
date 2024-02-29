import React from 'react'
import { Avatar,  Card, CardActions, CardContent,CardHeader, CardMedia, Checkbox, IconButton, Typography } from '@mui/material'
import MoreVertIcon from '@mui/icons-material/MoreVert';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShareIcon from '@mui/icons-material/Share';
import FavoriteBorder from '@mui/icons-material/FavoriteBorder';
import Favorite from '@mui/icons-material/Favorite';
import { useState, useEffect } from 'react';

function randomNumberInRange(min, max) {
    // 👇️ get number between min (inclusive) and max (inclusive)
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }



const Post = () => {
    const [imagePath, setImagePath] = useState("");   

    useEffect(() => {
        const fetchRandomImage = async () => {
          const randomNumber = randomNumberInRange(1, 1000);
          const imageURL = `https://source.unsplash.com/random?${randomNumber}`;
          setImagePath(imageURL);
        };
    
        fetchRandomImage();
      }, []); // Empty dependency array ensures the effect runs only once on component mount


  return (
    <Card sx={{margin:3}}>
        <CardHeader
        avatar={
            <Avatar sx={{ bgcolor: "red" }} aria-label="recipe">
            R
            </Avatar>
        }
        action={
            <IconButton aria-label="settings">
            <MoreVertIcon />
            </IconButton>
        }
        title="Shrimp and Chorizo Paella"
        subheader="September 14, 2016"
        />
        <CardMedia
        component="img"
        sx={{height:"400px", objectFit: "contain"}}
        image= {imagePath}
        alt="Paella dish"
        />
        <CardContent>
        <Typography variant="body2" color="text.secondary">
            This impressive paella is a perfect party dish and a fun meal to cook
            together with your guests. Add 1 cup of frozen peas along with the mussels,
            if you like.
        </Typography>
        </CardContent>
        <CardActions disableSpacing>
        <IconButton aria-label="add to favorites">
        <Checkbox  icon={<FavoriteBorder />} checkedIcon={<Favorite sx={{color:"red"}}  />} />
        </IconButton>
        <IconButton aria-label="share">
            <ShareIcon />
        </IconButton>
        </CardActions>
  </Card>
  )
}

export default Post