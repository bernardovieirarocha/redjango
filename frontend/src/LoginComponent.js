import React from "react";
import axios from "axios";
import UserList from "./userLists";

const url = "http://localhost:8081/api-token-auth/";

export default class LoginComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: "",
            errors: this.props.errors,
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value,
        });
    }
    handleSubmit(event) {
        const { username, password } = this.state;
        axios
            .post(url, {
                username: username,
                password: password,
            })
            .then((response) => {
                if (response.data.token) {
                    localStorage.setItem("access_token", response.data.token);
                    localStorage.setItem("email", response.data.email);
                    localStorage.setItem("userId", response.data.user_id);
                    this.setState({ token: response.data.token });
                }
            })
            .catch((error) => {
                console.log(error);
            });
        event.preventDefault();
    }

    render() {
        const token = localStorage.getItem("access_token");

        if (!token && !this.state.errors) {
            return (
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Username:
                        <input
                            id="username"
                            name="username"
                            autoComplete="Username"
                            type="text"
                            value={this.state.username}
                            onChange={this.handleChange}
                            placeholder="Username"
                        />
                    </label>
                    <label>
                        Password:
                        <input
                            id="password"
                            name="password"
                            autoComplete="password"
                            placeholder="Password"
                            type="password"
                            value={this.state.password}
                            onChange={this.handleChange}
                        />
                    </label>
                    <input type="submit" value="Submit" />
                </form>
            );
        } else {
            return <UserList />;
        }
    }
}
