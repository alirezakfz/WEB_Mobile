import React from "react";
import { Typography, AppBar, Card, CardActions, CardContent , CardMedia ,Grid, Button, CssBaseline, Toolbar, Container } from "@mui/material";
import { PhotoCamera } from "@mui/icons-material";
import { styled } from '@mui/material/styles';


// const containerClass = styled(CameraIcon)(
//     ({ theme}) => `
//     background-color : ${theme.palette.background.paper};
//     padding: ${theme.spacing(8,0,6)}
//     `,
// );

const cards = [1,2,3,4,5,6,7,8,9]

const App = () =>{
    
    return(
        <>
            <CssBaseline />
            <AppBar position="relative">
                <Toolbar>
                    <PhotoCamera sx={{marginRight: '20px'}}/>
                    <Typography variant="h6">Photo Album</Typography>
                </Toolbar>
            </AppBar>
            <main>
                <div className="container">
                    <Container maxWidth='sm' sx={{backgroundColor: 'background.paper',
                                                    padding: "40px 24px", }}>
                        <Typography variant="h2" align="center" color="textPrimary" gutterBottom >
                            Photo Albun
                        </Typography>
                        <Typography variant="h5" align="center" color="textSecondary" paragraph>
                            Hello This is photo album page. This is a project to learn Material UI. Its actually my first React project with Material UI.
                            Its a great library to use for developing apps with React.
                        </Typography>
                        <div>
                            <Grid container spacing={2} justify="center">
                                <Grid item>
                                    <Button variant="contained" color="primary" sx={{marginTop:'40px'}} >
                                        see my photos
                                    </Button>
                                </Grid>
                                <Grid item>
                                    <Button variant="contained" color="primary" sx={{marginTop:'40px'}}>
                                        see my photos
                                    </Button>
                                </Grid>
                            </Grid>
                        </div>
                    </Container>
                </div>
                <Container maxWidth="md">
                    <Grid container spacing={4}>
                        {cards.map( (card) => (
                            <Grid item  key={card} xs={12} sm={6} md={4} sx={{ padding: "20px 0"}}>
                            <Card sx ={{height: "100%",
                                    display: "flex",
                                    flexDirection: "column"
                                    }}>

                                <CardMedia 
                                image="https://source.unsplash.com/random"
                                title = "Image title"
                                sx={{
                                    paddingTop: "56.25%", //16:9
                                }}
                                />
                                <CardContent sx ={{flexGrow:1}} >
                                    <Typography gutterBottom variant = "h5">
                                        Heading
                                    </Typography>
                                    <Typography>
                                        This a media card. You can use it to describe the image.
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Button size="small" color="primary" >View</Button>
                                    <Button size="small" color="primary" >Edit</Button>
                                </CardActions>
                            </Card>
                        </Grid>
                        ))}
                    </Grid>
                </Container>
            </main>
            <footer>
                <Container align="center" sx={{
                    bgcolor: "secondary.main",
                    padding: "25px"
                }}>
                    <Typography>Footer</Typography>
                    <Typography variant="subtitle1" color="textSecondary">@2024 by Alireza</Typography>
                </Container> 
            </footer>
        </>
    );
}


export default App;