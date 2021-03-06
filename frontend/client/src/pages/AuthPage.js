import React, {useContext, useEffect, useState} from 'react'
import {useHttp} from "../hooks/http.hook";
import {useMessage} from "../hooks/message.hook";
import {AuthContext} from "../context/AuthContext";

export const AuthPage = () => {
    const auth = useContext(AuthContext)
    const message = useMessage()
    const {loading, error, request, clearError} = useHttp()
    const [form, setForm] = useState({
        email: '', password: ''
    })

    useEffect(() => {
            message(error)
            clearError()
        }, [error, message, clearError]
    )
    useEffect(()=>{
        window.M.updateTextFields()},[])
    const changeEventHandler = event => {
        setForm({...form, [event.target.name]: event.target.value})
    }

    const registerHandler = async () => {
        try {
            const data = await request('/api/auth/register', 'POST', {...form})
            console.log('Data', data)
        } catch (e) {

        }
    }
    const loginHandler = async () => {
        try {
            const data = await request('/api/auth/login', 'POST', {...form})
            auth.login(data.token, data.userId)
            console.log('Data', data)
        } catch (e) {

        }
    }
    return (
        <div className="row">
            <div className="col s6 offset-s3">
                <h1>Emotion Recognition</h1>
                <div className="card blue-grey darken-1">
                    <div className="card-content white-text">
                        <span className="card-title">Authorization</span>
                        <div>

                            <div className="input-field">
                                <label htmlFor="email">Email</label>
                                <input
                                    placeholder="Enter email"
                                    id="email"
                                    type="text"
                                    name="email"
                                    className="black-input"
                                    value={form.email}
                                    onChange={changeEventHandler}
                                />
                            </div>
                            <div className="input-field">
                                <label htmlFor="password">Password</label>
                                <input
                                    placeholder="Enter password"
                                    id="password"
                                    type="password"
                                    name="password"
                                    className="black-input"
                                    value={form.password}
                                    onChange={changeEventHandler}
                                />

                            </div>
                        </div>
                    </div>
                    <div className="card-action">
                        <button className="btn grey darken-4 white-text"
                                style={{marginRight: 10}}
                                onClick={loginHandler}
                                disabled={loading}>
                            Log in
                        </button>
                        <button
                            className="btn grey darken-4 white-text"
                            onClick={registerHandler}
                            disabled={loading}>
                            Sign in
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}
