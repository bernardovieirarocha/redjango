import React from "react";
import ListComponent from "./ListComponent";
import axios from "axios";


const url = "http://localhost:8081/list/";
export default class UserList extends React.Component {
    constructor(props) {
        super(props);
        this.state = { lists: [], loading: true, errors: "" };
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
                console.log(response.data);
                this.setState({ lists: response.data, loading: false });
            })
            .catch((error) => {
                if (error.response.status === 401) {
                    this.setState({ errors: "Unauthorized Token" });
                }
            });
    }

    render() {
        const listsApi = this.state.lists;


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
