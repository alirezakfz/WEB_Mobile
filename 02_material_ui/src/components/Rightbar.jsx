import { Avatar, AvatarGroup, Box, ImageList, ImageListItem, Typography } from '@mui/material'
import React from 'react'
import { Conversations } from './Conversations';

function randomNumberInRange(min, max) {
  // 👇️ get number between min (inclusive) and max (inclusive)
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

export const Rightbar = () => {
  const list = [1,2,3,4,5,6,7,8,9,10,11,12]
  return (
    <Box //bgcolor="green" 
    flex={2} 
    p={2}
    sx={{display: {xs: "none", sm:"block"}}}
    >
       <Box 
       //position='fixed'
       >
        <Typography variant='h6' fontWeight={100}>Online Freinds</Typography>
        <AvatarGroup max={4}>
          <Avatar alt="Remy Sharp" src="/static/images/avatar/1.jpg" />
          <Avatar alt="Travis Howard" src="/static/images/avatar/2.jpg" />
          <Avatar alt="Cindy Baker" src="/static/images/avatar/3.jpg" />
          <Avatar alt="Agnes Walker" src="/static/images/avatar/4.jpg" />
          <Avatar alt="Trevor Henderson" src="/static/images/avatar/5.jpg" />
        </AvatarGroup>
        <Typography variant='h6' fontWeight={100} mt={2} mb={2}>Latest Photos</Typography>
          <ImageList cols={4} gap={5}>
            {list.map((i, index) => (
              <ImageListItem key={index}> {/* Add a unique key for each item */}
                <img
                  src={`https://source.unsplash.com/random?${randomNumberInRange(1,500)}`}
                  alt=""
                />
              </ImageListItem>
            ))}
          </ImageList>
          <Typography variant='h6' fontWeight={100} mt={2} mb={2}>Latest Conversations</Typography>
          <Conversations />
       </Box>
    </Box>
  )
}
