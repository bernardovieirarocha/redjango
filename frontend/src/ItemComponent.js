import React from "react";

export default function ItemComponent(props) {
    return (
        <li>
            {props.name}
            <div>
                {props.status ? <p>Não Finalizado</p> : <p>Completo</p>}
            </div>
        </li>
    );
}
