import React from "react";

import Card from '../UI/Card';
import Alumno from "./Alumno/Alumno";
import './Alumnos.css';

const Alumnos = (props) => {  
    return (
        <div>
            <Card className='alumnos'>
                <Alumno
                    nombre={props.alumnos[0].nombre}
                    apellido={props.alumnos[0].apellido}
                    numCta={props.alumnos[0].numCta}
                />
                <Alumno
                    nombre={props.alumnos[1].nombre}
                    apellido={props.alumnos[1].apellido}
                    numCta={props.alumnos[1].numCta}
                />
                <Alumno
                    nombre={props.alumnos[2].nombre}
                    apellido={props.alumnos[2].apellido}
                    numCta={props.alumnos[2].numCta}
                />
            </Card>
        </div>
    )
};

export default Alumnos;