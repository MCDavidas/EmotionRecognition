import React from 'react'
import {CameraPage} from "./pages/CameraPage";
import Switch from "react-router-dom/es/Switch";
import Route from "react-router-dom/es/Route";
import {CreatePage} from "./pages/CreatePage";
import {DetailPage} from "./pages/DetailPage";
import Redirect from "react-router-dom/es/Redirect";
import {AuthPage} from "./pages/AuthPage";

export const useRoutes = isAuthenticated => {
    if(isAuthenticated){
        return(
            <Switch>
                <Route path="/camera" exact>
                    <CameraPage />
                </Route>
                <Route path="/create" exact>
                    <CreatePage />
                </Route>
                <Route path="/detail/:id" exact>
                    <DetailPage />
                </Route>
                <Redirect to="/camera" />
            </Switch>
        )
    }
    return(
        <Switch>
            <Route path="/" exact>
                <AuthPage />
            </Route>
            <Redirect to="/" />
        </Switch>
    )
}
