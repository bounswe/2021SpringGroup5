import * as React from 'react';
import { styled, useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import MuiDrawer from '@mui/material/Drawer';
import MuiAppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import CssBaseline from '@mui/material/CssBaseline';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import AccountCircle from '@mui/icons-material/AccountCircle';
import { Add, Home, Logout, Search } from '@mui/icons-material';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import { useHistory } from 'react-router';

// #f8f8f8 background

const drawerWidth = 240;

const openedMixin = (theme) => ({
  width: drawerWidth,
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: 'hidden',
});

const closedMixin = (theme) => ({
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: 'hidden',
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up('sm')]: {
    width: `calc(${theme.spacing(9)} + 1px)`,
  },
});

const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'flex-end',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({
    width: drawerWidth,
    flexShrink: 0,
    whiteSpace: 'nowrap',
    boxSizing: 'border-box',
    ...(open && {
      ...openedMixin(theme),
      '& .MuiDrawer-paper': openedMixin(theme),
    }),
    ...(!open && {
      ...closedMixin(theme),
      '& .MuiDrawer-paper': closedMixin(theme),
    }),
  }),
);

export default function MiniDrawer() {
  const theme = useTheme();
  const history = useHistory()

  const [open, setOpen] = React.useState(false);

  const handleDrawerOpen = () => {
    document.body.classList.add('modal-open');
    setOpen(true);
  };

  const handleDrawerClose = () => {
    document.body.classList.remove('modal-open');
    setOpen(false);
  };

  const [anchorEl, setAnchorEl] = React.useState(null);
  const openCreateMenu = Boolean(anchorEl);
  const handleOpenCreateMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleCloseCreateMenu = () => {
    setAnchorEl(null);
  };

  const handleLogout = () => {
    window.localStorage.removeItem("token");
    history.push("/login")
  };

  return (
    <>
      <Box sx={{ display: 'flex' }}>
        <CssBaseline />
        <AppBar position="fixed" open={open} className="bg-white">
          <Toolbar>
            <IconButton
              aria-label="open drawer"
              onClick={handleDrawerOpen}
              edge="start"
              sx={{
                marginRight: '36px',
                ...(open && { display: 'none' }),
              }}
            >
              <MenuIcon />
            </IconButton>
            <Typography style={{ color: "black" }} variant="h6" component="div" className="fs-4 fw-bolder" sx={{ flexGrow: 1 }}>
              Ludo
            </Typography>
          </Toolbar>
        </AppBar>
        <Drawer variant="permanent" open={open}>
          <DrawerHeader>
            <IconButton onClick={handleDrawerClose}>
              {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
            </IconButton>
          </DrawerHeader>
          <Divider />
          <List>
            <ListItem button key={1} onClick={() => history.push("/")}>
              <ListItemIcon>
                <Home />
              </ListItemIcon>
              <ListItemText primary={"Home"} />
            </ListItem>
            <ListItem button key={2} onClick={() => history.push("/search")}>
              <ListItemIcon>
                <Search />
              </ListItemIcon>
              <ListItemText primary={"Search"} />
            </ListItem>
            <ListItem button key={3} onClick={handleOpenCreateMenu}>
              <ListItemIcon>
                <Add />
              </ListItemIcon>
              <ListItemText primary={"Create"} />
            </ListItem>
            <Menu
              id="basic-menu"
              anchorEl={anchorEl}
              open={openCreateMenu}
              onClose={handleCloseCreateMenu}
              MenuListProps={{
                'aria-labelledby': 'basic-button',
              }}
            >
              <MenuItem onClick={() => history.push("/createEvent") && handleCloseCreateMenu}>Create Event Post</MenuItem>
              <MenuItem onClick={() => history.push("/createEquipment") && handleCloseCreateMenu}>Create Equipment Post</MenuItem>
            </Menu>
            <ListItem button key={3} onClick={() => history.push("/profile")}>
              <ListItemIcon>
                <AccountCircle />
              </ListItemIcon>
              <ListItemText primary={"Profile"} />
            </ListItem>
          </List>
          <Divider />
          <List>
            <ListItem button key={1} onClick={handleLogout}>
              <ListItemIcon>
                <Logout />
              </ListItemIcon>
              <ListItemText primary={"Log out"} />
            </ListItem>
          </List>
        </Drawer>
        <DrawerHeader />
      </Box>
    </>
  );
}
