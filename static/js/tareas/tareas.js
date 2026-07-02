function agregarImagen() {
    const div = document.createElement('div');
    div.innerHTML = '<input type="file" name="imagenes">';
    document.getElementById('imagenes-container').appendChild(div);
}

function agregarArchivo() {
    const div = document.createElement('div');
    div.innerHTML = '<input type="file" name="archivos">';
    document.getElementById('archivos-container').appendChild(div);
}

function agregarVideo() {
    const div = document.createElement('div');
    div.innerHTML = '<input type="url" name="videos" placeholder="https://youtube.com/...">';
    document.getElementById('videos-container').appendChild(div);
}



let contadorPreguntas = 0;

document.addEventListener("DOMContentLoaded", () => {
    agregarPregunta();
});

function agregarPregunta() {

    const indice = contadorPreguntas;

    const card = document.createElement("div");
    card.className = "card mt-3 p-3";

    card.innerHTML = `
        <h5>Pregunta ${indice + 1}</h5>

        <label>Enunciado</label>
        <textarea
            name="pregunta_${indice}"
            class="form-control">
            </textarea>

        <br>

        <label>Tipo</label>

        <select
            id="tipo-${indice}"
            name="tipo_${indice}"
            class="form-control"
            onchange="cambiarTipo(this, ${indice})">

            <option value="texto">Respuesta abierta</option>
            <option value="opcion">Opción múltiple</option>

        </select>

        <br>

        <label>Puntaje</label>
        <input
            type="number"
            name="puntaje_${indice}"
            value="1"
            class="form-control">

        <br>

        <div id="contenido-${indice}"></div>
    `;

    document.getElementById("preguntas-container").appendChild(card);

    cambiarTipo(document.getElementById(`tipo-${indice}`), indice);

    contadorPreguntas++;
}

function cambiarTipo(select, indice) {

    const contenedor = document.getElementById(`contenido-${indice}`);

    if (!contenedor) return;

    if (select.value === "texto") {

        contenedor.innerHTML = `
            <label>Respuesta correcta</label>

            <input type="text" name="respuesta_correcta_${indice}" class="form-control">`;

    } else {

        contenedor.innerHTML = `
            <label>A</label>
            <input
                type="text"
                name="opciones_${indice}[]"
                class="form-control mb-2">

            <label>B</label>
            <input
                type="text"
                name="opciones_${indice}[]"
                class="form-control mb-2">

            <label>C</label>
            <input
                type="text"
                name="opciones_${indice}[]"
                class="form-control mb-2">

            <label>D</label>
            <input
                type="text"
                name="opciones_${indice}[]"
                class="form-control mb-2">

            <label>Respuesta correcta</label>

            <select
                name="correcta_${indice}"+
                class="form-control">

                <option value="A">A</option>
                <option value="B">B</option>
                <option value="C">C</option>
                <option value="D">D</option>

            </select>
        `;
    }
}

