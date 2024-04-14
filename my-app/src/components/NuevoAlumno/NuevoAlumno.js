import React from "react";

import './NuevoAlumno.css';
import AlumnoForm from "./AlumnoForm/AlumnoForm";

const NuevoAlumno = (props) => {
    
    const guardaAlumnoHandler = (alumnoIngresado) => {
        const alumnos = { 
            ...alumnoIngresado
        };
        props.onAgregarAlumno(alumnos);
    };

    return (
        <div className="nuevo-alumno">
            <AlumnoForm onGuardarAlumno={guardaAlumnoHandler} />
        </div>
    )
}

export default NuevoAlumno;