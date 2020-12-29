/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dto;

/**
 *
 * @author heloh
 */
public class Exame {

    private String caracteristicatecido;
    private String classeanormalidade;
    private String gravidadeanormalidade;
    private String nomeimagem;
    private Integer x;
    private Integer y;
    private Integer raio;

    private int paciente_idpaciente;
    private int paciente_cpf;

    public String getCaracteristicatecido() {
        return caracteristicatecido;
    }

    public void setCaracteristicatecido(String caracteristicatecido) {
        this.caracteristicatecido = caracteristicatecido;
    }

    public String getClasseanormalidade() {
        return classeanormalidade;
    }

    public void setClasseanormalidade(String classeanormalidade) {
        this.classeanormalidade = classeanormalidade;
    }

    public String getGravidadeanormalidade() {
        return gravidadeanormalidade;
    }

    public void setGravidadeanormalidade(String gravidadeanormalidade) {
        this.gravidadeanormalidade = gravidadeanormalidade;
    }

    public Integer getX() {
        return x;
    }

    public void setX(Integer x) {
        this.x = x;
    }

    public Integer getY() {
        return y;
    }

    public void setY(Integer y) {
        this.y = y;
    }

    public Integer getRaio() {
        return raio;
    }

    public void setRaio(Integer raio) {
        this.raio = raio;
    }

    public int getPaciente_idpaciente() {
        return paciente_idpaciente;
    }

    public void setPaciente_idpaciente(int paciente_idpaciente) {
        this.paciente_idpaciente = paciente_idpaciente;
    }

    public int getPaciente_cpf() {
        return paciente_cpf;
    }

    public void setPaciente_cpf(int paciente_cpf) {
        this.paciente_cpf = paciente_cpf;
    }

    public String getNomeimagem() {
        return nomeimagem;
    }

    public void setNomeimagem(String nomeimagem) {
        this.nomeimagem = nomeimagem;
    }

}
