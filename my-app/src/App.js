import React, { useState } from "react";

import "./App.css";

import Alumnos from "./components/Alumnos/Alumnos";
import NuevoAlumno from "./components/NuevoAlumno/NuevoAlumno";

function App() {
  const [peliculas, setPeliculas] = useState([
    { id: 1, title: "Spiderman", director: "Sam R." },
    { id: 2, title: "Batman", director: "Tim Burton" },
    { id: 3, title: "Inception", director: "Christopher Nolan", inventario: 4 },
  ]);

  const [alumnos, setAlumnos] = useState([
    {
      nombre: "Fernando",
      apellido: "Fong",
      numCta: 313320679,
    },
    {
      nombre: "Valeria",
      apellido: "Garcia",
      numCta: 314006088,
    },
    {
      nombre: "Erick",
      apellido: "Martinez",
      numCta: 414890123,
    },
  ]);

  const agregarAlumno = (alumno) => {
    const nuevoAlumno = [alumno, ...alumnos];
    setAlumnos(nuevoAlumno);
    console.log(nuevoAlumno);
  };

  return (
    <div className="App">
      <NuevoAlumno onAgregarAlumno={agregarAlumno} />
      <Alumnos alumnos={alumnos} />
    </div>
  );
}

export default App;
