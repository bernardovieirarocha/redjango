import React from "react";
import ListComponent from "./ListComponent";
import LoginComponent from "./LoginComponent";
import axios from "axios";

const url = "http://localhost:8000/list/";
export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = { lists: [], loading: true, token: localStorage.getItem('access_token') };
    }

    async componentDidMount() {
        
        axios
            .get(url, {
                headers: {
                    Authorization:
                        "Token " + localStorage.getItem("access_token"),
                },
            })
            .then((response) => {
                console.log(response.data)
                this.setState({ lists: response.data, loading: false });

            })
            .catch((error) => {
                if(error.response.status === 401) {
                    this.setState({token: ''})
                }
            });

     
    }

    render() {
        const listsApi = this.state.lists;

        if (!this.state.token) {
            return ( <LoginComponent /> );
        } else {
            return (
                <div>
                    {listsApi.map((list) => (
                        <ListComponent
                            key={list.id}
                            listName={list.name}
                            items={list.item_set}
                        />
                    ))}
                </div>
            );
        }
    }
}
