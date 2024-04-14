import React from "react";

import Card from '../../UI/Card';
import './Alumno.css';

const Alumno = (props) => {
    return (
        <Card className='alumno'>
            <div className="alumno__description">
                <h2>{props.nombre}</h2>
                <h2>{props.apellido}</h2>
                <h2>{props.numCta}</h2>
            </div>
        </Card>
    );
}

export default Alumno