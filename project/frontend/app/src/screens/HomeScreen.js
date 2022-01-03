import './Home.css';

function HomeScreen() {

    return (
        <div className="container_home">
            <img className="logo_home" src="https://cdn.discordapp.com/attachments/825091092374356030/907634507308490772/1.png" />
            <span className="text_home">Our project is creating an amateur sports coordination platform. The main virtue osf the platform i that it brings people that are interested same kind of sports together so that they can meet new people, socialize and engage in sports they like. In addition to that, people can create accounts for commercial purposes for example sport shop owners or sport field owners can create an account in the name of their business, create posts and participate events like every other user can do.</span>
            <h1>Favourite Sport Categories</h1>
            <div className="banners">
                <a href="/search" className="banner">
                    <img src="https://www.recablog.com/wp-content/uploads/2021/01/soccer-780x470.jpg"/>
                    <span>Soccer</span>
                </a>
                <a href="/search" className="banner">
                    <img src="https://sawahpress.com/en/wp-content/uploads/2021/11/thumbs_b_c_fec562758581b280dd2514fd42698034-780x470.jpg"/>
                    <span>Basketball</span>
                </a>
                <a href="/search" className="banner">
                    <img src="https://gulfgoal.com/en/wp-content/uploads/2021/12/urn-newsml-dpa-com-20090101-211118-99-48608_large_4_3-780x470.jpg"/>
                    <span>Tennis</span>
                </a>
            </div>
            
        </div>
    );
}

export default HomeScreen;
