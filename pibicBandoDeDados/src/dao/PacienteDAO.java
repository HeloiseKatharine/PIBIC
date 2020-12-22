package dao;

import dto.Paciente;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class PacienteDAO {

    Connection conn;
    PreparedStatement pstm;
    ResultSet rs;
    ArrayList<Paciente> lista = new ArrayList<>();

    public void cadastrarPaciente(Paciente objPaciente) {

        String sql = "insert into paciente (cpf, nome) values (?,?)";

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

        public ResultSet pesquisarPaciente(Paciente objPaciente) {

        conn = new ConexaoDAO().conexaoBD();

        try {

            String sql = "select cpf, nome from paciente where cpf = ? and nome = ?; ";
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

    /* 
    
    public ArrayList<Paciente> pesquisarPaciente() {

        String sql = "select * from paciente";

        try {

            pstm = conn.prepareStatement(sql);
            rs = pstm.executeQuery();

            while (rs.next()) {

                Paciente objPaciente = new Paciente();

                objPaciente.setId_paciente(rs.getInt("idpaciente"));
                objPaciente.setCpf(rs.getString("cpf"));
                objPaciente.setNome(rs.getString("nome"));

                lista.add(objPaciente);
            }

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO pesquisar: " + e);
        }
        return lista;*/
}
