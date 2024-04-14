import React, { useState } from "react";

import "./AlumnoForm.css";

const AlumnoForm = (props) => {
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [apellidoIngresado, setApellidoIngresado] = useState("");
  const [numCtaIngresado, setNumCtaIngresado] = useState("");

  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioApellidoHandler = (event) => {
    setApellidoIngresado(event.target.value);
  };

  const cambioNumCtaHandler = (event) => {
    setNumCtaIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const alumno = {
      nombre: nombreIngresado,
      apellido: apellidoIngresado,
      numCta: numCtaIngresado,
    };
    if (
      nombreIngresado === "" ||
      apellidoIngresado === "" ||
      numCtaIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarAlumno(alumno);
    setNombreIngresado("");
    setApellidoIngresado("");
    setNumCtaIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="nuevo-alumno__controls">
        <div className="nuevo-alumno__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
        <div className="nuevo-alumno__control">
          <label>Apellido: </label>
          <input
            type="text"
            value={apellidoIngresado}
            onChange={cambioApellidoHandler}
          />
        </div>
        <div className="nuevo-alumno__control">
          <label>Num. Cta.: </label>
          <input
            type="text"
            value={numCtaIngresado}
            onChange={cambioNumCtaHandler}
          />
        </div>
        <div className="nuevo-alumno__actions">
          <button type="submit">Agregar alumno</button>
        </div>
      </div>
    </form>
  );
};

export default AlumnoForm;
