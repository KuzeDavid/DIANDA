// EstadoEstudianteService.cs
//Solo para usar si no tenemos BD

public class EstadoEstudianteService
{
    public bool EsEstudiante { get; private set; }

    public void EstablecerComoEstudiante()
    {
        EsEstudiante = true;
    }

    public void EstablecerComoNoEstudiante()
    {
        EsEstudiante = false;
    }
}
