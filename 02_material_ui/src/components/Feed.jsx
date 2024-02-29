import { Box, Grid} from '@mui/material'
import React from 'react'
import Post from './Post'


export const Feed = () => {
  const list = [1,2,3,4,5,6]

  return (
    <Box //bgcolor="pink" 
    flex={4} p={2}>
      <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 3, md: 3 }}>
          {list.map( (i, index) => (<Grid item  key={index} xs={12} sm={6} ><Post /></Grid>))}
      </Grid>
       <Post />
    </Box>
  )
}
