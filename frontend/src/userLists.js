import React from "react";
import ListComponent from "./ListComponent";
import ItemComponent from "./ItemComponent";

export default function UserLists() {
    return (
        <div>
            <ListComponent listName={"Minha Lista"} />
            <ListComponent listName={"Minha Lista"} />
        </div>
    );
}
