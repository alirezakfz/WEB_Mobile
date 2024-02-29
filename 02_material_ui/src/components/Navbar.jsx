
import { AppBar, Box, InputBase, Typography } from '@mui/material'
import React from 'react'
import Pets from '@mui/icons-material/Pets';
import { styled } from '@mui/system';
import Toolbar from '@mui/material/Toolbar';
import Badge from '@mui/material/Badge';
import MailIcon from '@mui/icons-material/Mail';
import NotificationsIcon from '@mui/icons-material/Notifications';
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

const StyledToolbar = styled(Toolbar)({
    display: "flex",
    flexDirection:"row",
    justifyContent: "space-between",
});

const Search = styled("div") (({ theme }) => ({
    backgroundColor : "white",
    color: "black",
    padding: "0 10px",
    borderRadius: theme.shape.borderRadius,
    width:"40%"
}));
    
const Icons = styled(Box)(({ theme }) => ({
    display: "none",
    gap: "20px",
    alignItems: "center",
    [theme.breakpoints.up("sm")]:{
        display: "flex"
    },
    color:"black"
}));


const UserBox = styled(Box)(({ theme }) => ({
    display: "flex",
    gap: "10px",
    alignItems: "center",
    [theme.breakpoints.up("sm")]:{
        display: "none"
    },
}));


function Navbar() {
    const [open, setOpen] = React.useState(null);
    
  return (
    <AppBar position="sticky">
        <StyledToolbar>
            <Typography variant="h6" sx={{ display:{xs:"none", sm:"block"}}}>LAMA DEV</Typography>
            <Pets sx={{ display:{xs:"block", sm:"none"}}}/>
            <Search><InputBase placeholder='search'/></Search>
            <Icons >
                <Badge badgeContent={4} color="error">
                    <MailIcon  />
                </Badge>
                <Badge badgeContent={3} color="error">
                    <NotificationsIcon  />
                </Badge>
                <Avatar 
                    sx={{width:"30px", height:"30px"}} 
                    alt="R" 
                    src="/static/images/avatar/1.jpg" 
                    onClick = {e=>setOpen(true)}/>
            </Icons>
            <UserBox>
                <Avatar 
                sx={{width:"30px", height:"30px"}} 
                alt="R" 
                src="/static/images/avatar/1.jpg" 
                onClick = {e=>setOpen(true)}/>
                <Typography>John</Typography>
            </UserBox>
        </StyledToolbar>

        <Menu
            id="demo-positioned-menu"
            aria-labelledby="demo-positioned-button"
            
            open={open}
            onClose={e=>setOpen(false)}
            anchorOrigin={{
            vertical: 'top',
            horizontal: 'right',
            }}
            transformOrigin={{
            vertical: 'top',
            horizontal: 'right',
            }}
        >
        <MenuItem >Profile</MenuItem>
        <MenuItem >My account</MenuItem>
        <MenuItem >Logout</MenuItem>
      </Menu>

    </AppBar>
  )
}

export default Navbar