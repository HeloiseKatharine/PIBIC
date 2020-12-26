/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dao;

import dto.Paciente;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 *
 * @author heloh
 */
public class ExameDAO {

    Connection conn;
    PreparedStatement pstm;
    ResultSet rs;
    ArrayList<Paciente> lista = new ArrayList<>();

    public void cadastrarExame(Paciente objPaciente) {

        String sql = "insert into paciente (cpf, nome) values (?,?);";

        conn = new ConexaoDAO().conexaoBD();

        try {

            pstm = conn.prepareStatement(sql);
            pstm.setString(1, objPaciente.getCpf());/*para ?*/
            pstm.setString(2, objPaciente.getNome());

            pstm.execute();
            pstm.close();

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO " + e);
        }
    }

    /*public ResultSet pesquisarExame(Paciente objPaciente) {

        conn = new ConexaoDAO().conexaoBD();

        try {

            String sql = "select cpf, nome from paciente where cpf = ? and nome = ? ";
            pstm = conn.prepareStatement(sql);

            pstm.setString(1, objPaciente.getCpf());
            pstm.setString(2, objPaciente.getNome());

            rs = pstm.executeQuery();
            return rs;

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO: " + e);
            return null;
        }
    }*/

   /* public boolean mostrarExame(Paciente objPaciente) {

        conn = new ConexaoDAO().conexaoBD();

        try {

            String sql = "select * from paciente where cpf = ?; ";
            pstm = conn.prepareStatement(sql);

            pstm.setString(1, objPaciente.getCpf());

            rs = pstm.executeQuery();

            //pesquisando no banco
            if (rs.next()) {

                objPaciente.setCpf(rs.getString("cpf"));
                objPaciente.setNome(rs.getString("nome"));
            }

            return true;

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO: " + e);
            return false;
        }
    }*/
}
