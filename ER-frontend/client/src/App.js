import 'materialize-css'
import {BrowserRouter as Router} from 'react-router-dom'
import {useRoutes} from "./routes";
import {useAuth} from "./hooks/auth.hook";
import {Navbar} from "./components/Navbar";
import {AuthContext} from "./context/AuthContext";


function App() {
    const {token, login, logout, userId} = useAuth()
    const isAuthenticated = !!token
    const routes = useRoutes(isAuthenticated)

    return (
        <AuthContext.Provider value ={{
            token,login,logout,userId, isAuthenticated
<<<<<<< HEAD
        }} >
=======
        }}>
>>>>>>> liubov-frontend
            <Router>
                {
                    isAuthenticated && <Navbar />
                }
<<<<<<< HEAD
                <div  className="container">
=======
                <div className="container">
>>>>>>> liubov-frontend
                    {routes}
                </div>
            </Router>
        </AuthContext.Provider>
    )
}

export default App;
