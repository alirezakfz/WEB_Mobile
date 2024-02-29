import { Box } from '@mui/material'
import React from 'react'
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import HomeIcon from '@mui/icons-material/Home';
import DescriptionIcon from '@mui/icons-material/Description';
import GroupsIcon from '@mui/icons-material/Groups';
import StorefrontIcon from '@mui/icons-material/Storefront';
import SettingsIcon from '@mui/icons-material/Settings';
import Switch from '@mui/material/Switch';
import ModeNightIcon from '@mui/icons-material/ModeNight';

const label = { inputProps: { 'aria-label': 'Switch demo' } };

export const Sidebar = ({mode, setMode}) => {

  return (
    <Box //bgcolor="skyblue" 
    flex={1} 
    p={2} 
    sx={{display: {xs: "none", sm:"block"}}}
    >
        <Box position='fixed'>
        <List>
          <ListItem disablePadding>
            <ListItemButton component="a" href="#home" >
              <ListItemIcon>
                <HomeIcon />
              </ListItemIcon>
              <ListItemText primary="Homepage" />
            </ListItemButton>
          </ListItem>
          </List>

          <List>
          <ListItem disablePadding>
            <ListItemButton component="a" href="#pages" >
              <ListItemIcon>
                <DescriptionIcon />
              </ListItemIcon>
              <ListItemText primary="Pages" />
            </ListItemButton>
          </ListItem>
          </List>

          <List>
          <ListItem disablePadding>
            <ListItemButton component="a" href="#groups" >
              <ListItemIcon>
                <GroupsIcon />
              </ListItemIcon>
              <ListItemText primary="Groups" />
            </ListItemButton>
          </ListItem>
          </List>

          <List>
          <ListItem disablePadding>
            <ListItemButton component="a" href="#marketplace" >
              <ListItemIcon>
                <StorefrontIcon />
              </ListItemIcon>
              <ListItemText primary="Marketplace" />
            </ListItemButton>
          </ListItem>
          </List>

          <List>
          <ListItem disablePadding>
            <ListItemButton component="a" href="#settings" >
              <ListItemIcon>
                <SettingsIcon />
              </ListItemIcon>
              <ListItemText primary="Settings" />
            </ListItemButton>
          </ListItem>
          </List>

          <List>
          <ListItem disablePadding>
            <ListItemButton component="a" href="#settings" >
              <ListItemIcon>
                <ModeNightIcon />
              </ListItemIcon>
              <Switch {...label} defaultChecked onChange={e => setMode(mode ==='light' ? 'dark' : 'light')}/>
            </ListItemButton>
          </ListItem>
          </List>
        </Box>
    </Box>
  )
}
