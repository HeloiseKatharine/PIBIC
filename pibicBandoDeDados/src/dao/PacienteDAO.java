package dao;

import dto.Exame;
import dto.Paciente;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Types;
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class PacienteDAO {

    Connection conn;
    PreparedStatement pstm;
    ResultSet rs;
    ArrayList<Paciente> lista = new ArrayList<>();

    public void cadastrarPaciente(Paciente objPaciente, Exame objExame) {

        String sql = "insert into paciente (cpf, nome) values (?,?);";
        String sql2 = " insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, paciente_cpf, paciente_idpaciente) values(?, ?, ?, ?, ?, ?, ?, LAST_INSERT_ID()); ";
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

        try {
            pstm = conn.prepareStatement(sql2);
            pstm.setString(1, objExame.getCaracteristicatecido());
            pstm.setString(2, objExame.getClasseanormalidade());
            pstm.setString(3, objExame.getGravidadeanormalidade());

            if (objExame.getX() == null) {
                pstm.setNull(4, Types.INTEGER);
            } else {
                pstm.setInt(4, objExame.getX());
            }

            if (objExame.getY() == null) {
                pstm.setNull(5, Types.INTEGER);
            } else {
                pstm.setInt(5, objExame.getY());
            }

            if (objExame.getRaio()== null) {
                pstm.setNull(6, Types.INTEGER);
            } else {
                pstm.setInt(6, objExame.getRaio());
            }

            pstm.setString(7, objPaciente.getCpf());

            pstm.execute();
            pstm.close();

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO " + e);
        }
    }

    public ResultSet pesquisarPaciente(Paciente objPaciente) {

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
    }

    public boolean mostrarPaciente(Paciente objPaciente) {

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
    }

}
