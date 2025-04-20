import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Activate from './containers/Activate';
import Home from './containers/Home';
import Login from './containers/Login';
import ResetPassword from './containers/ResetPassword';
import ResetPasswordConfirm from './containers/ResetPasswordConfirm';
import Signup from './containers/Signup';
import Layout from './hocs/Layout';

import { Provider } from 'react-redux';
import store from './store';

const App = () => (
    <Provider store={store}>
        <Router>
            <Layout>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/signup" element={<Signup />} />
                    <Route path="/reset-password" element={<ResetPassword />} />
                    <Route path="/password/reset/confirm/:uid/:token" element={<ResetPasswordConfirm />} />
                    <Route path="/activate/:uid/:token" element={<Activate />} />
                </Routes>
            </Layout>
        </Router>
    </Provider>
);


export default App; 