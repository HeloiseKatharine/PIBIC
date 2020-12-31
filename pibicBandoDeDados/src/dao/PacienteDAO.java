package dao;

import dto.Exame;
import dto.Paciente;
import java.io.File;
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
    PreparedStatement pstm2;
    ResultSet rs2;

    ResultSet rs;
    ArrayList<Exame> lista = new ArrayList<>();

    public void cadastrarPaciente(Paciente objPaciente, Exame objExame, boolean img) {

        String sql = "insert into paciente (cpf, nome) values (?,?);";
        String sql2 = " insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf, paciente_idpaciente) values(?, ?, ?, ?, ?, ?, ?, ?, LAST_INSERT_ID()); ";
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

        if (img == true) {

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

                if (objExame.getRaio() == null) {
                    pstm.setNull(6, Types.INTEGER);
                } else {
                    pstm.setInt(6, objExame.getRaio());
                }

                pstm.setString(7, objExame.getNomeimagem());
                pstm.setString(8, objPaciente.getCpf());

                pstm.execute();
                pstm.close();

            } catch (SQLException e) {
                JOptionPane.showMessageDialog(null, "PacienteDAO " + e);
            }
        }
    }

    public void cadastrarExame(Paciente objPaciente, Exame objExame, boolean img) {
        String sql = " insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem,paciente_cpf,  paciente_idpaciente) values(?, ?, ?, ?, ?, ?, ?,?, ?); ";

        conn = new ConexaoDAO().conexaoBD();
        if (img == true) {

            try {
                pstm = conn.prepareStatement(sql);
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

                if (objExame.getRaio() == null) {
                    pstm.setNull(6, Types.INTEGER);
                } else {
                    pstm.setInt(6, objExame.getRaio());
                }

                pstm.setString(7, objExame.getNomeimagem());
                pstm.setString(8, objPaciente.getCpf());
                pstm.setInt(9, objPaciente.getId_paciente());

                pstm.execute();
                pstm.close();

            } catch (SQLException e) {
                JOptionPane.showMessageDialog(null, "PacienteDAO " + e);
            }
        }
    }

    public ResultSet pesquisarPaciente(Paciente objPaciente) {

        conn = new ConexaoDAO().conexaoBD();

        try {

            String sql = "select cpf, nome from paciente where cpf = (?) and nome = (?); ";
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

    public boolean mostrarPaciente(Paciente objPaciente, Exame objExame) {

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
                objPaciente.setId_paciente(rs.getInt("idpaciente"));

                try {

                    String sql2 = "select * from exame where paciente_cpf = ?;";
                    pstm2 = conn.prepareStatement(sql2);

                    pstm2.setString(1, objPaciente.getCpf());

                    rs2 = pstm2.executeQuery();

                    //pesquisando no banco
                    if (rs2.next()) {

                        objExame.setCaracteristicatecido(rs2.getString("caracteristicatecido"));
                        objExame.setClasseanormalidade(rs2.getString("classeanormalidade"));
                        objExame.setGravidadeanormalidade(rs2.getString("gravidadeanormalidade"));
                        objExame.setX(rs2.getInt("x"));
                        objExame.setY(rs2.getInt("y"));
                        objExame.setRaio(rs2.getInt("raio"));

                    }
                    return true;

                } catch (SQLException e) {
                    JOptionPane.showMessageDialog(null, "PacienteDAO: " + e);
                    return false;
                }
            }

            return true;

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO: " + e);
            return false;
        }
    }

    public ArrayList<Exame> listarExames(Paciente objPaciente) {

        conn = new ConexaoDAO().conexaoBD();

        String sql = "select * from exame where  paciente_idpaciente = ?";

        try {
            pstm = conn.prepareStatement(sql);
            pstm.setInt(1, objPaciente.getId_paciente());

            rs = pstm.executeQuery();

            while (rs.next()) {
                Exame objExame = new Exame();
                objExame.setCaracteristicatecido(rs.getString("caracteristicatecido"));
                objExame.setClasseanormalidade(rs.getString("classeanormalidade"));
                objExame.setGravidadeanormalidade(rs.getString("gravidadeanormalidade"));
                objExame.setX(rs.getInt("x"));
                objExame.setY(rs.getInt("y"));
                objExame.setRaio(rs.getInt("raio"));
                objExame.setNomeimagem(rs.getString("nomeimagem"));

                lista.add(objExame);
            }
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "CinexaoDAO: " + e);
            return null;
        }
        return lista;
    }

    public void EditarPaciente(Paciente objPaciente) {

        String sql = "update paciente set cpf = ?, nome = ? where idpaciente = ?;";

        conn = new ConexaoDAO().conexaoBD();

        try {
            pstm = conn.prepareStatement(sql);

            pstm.setString(1, objPaciente.getCpf());
            pstm.setString(2, objPaciente.getNome());
            pstm.setInt(3, objPaciente.getId_paciente());

            pstm.execute();
            pstm.close();
            JOptionPane.showMessageDialog(null, "Editado com sucesso.");

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO " + e);
        }
    }

    public void ExcluirPaciente(Paciente objPaciente, Exame objExame) {

        String sql = "delete from  exame where paciente_idpaciente = ?; ";
        String sql2 = "delete from paciente where  idpaciente = ?; ";

        conn = new ConexaoDAO().conexaoBD();

        String nome = objExame.getNomeimagem();

        //deleta a imagem na pasta
        try {
            File imagem = new File("..\\imagens\\" + nome);
            imagem.delete();

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "TelaPaciente " + e);
        }

        try {
            pstm = conn.prepareStatement(sql);

            pstm.setInt(1, objPaciente.getId_paciente());

            pstm.execute();
            pstm.close();

            pstm2 = conn.prepareStatement(sql2);

            pstm2.setInt(1, objPaciente.getId_paciente());

            pstm2.execute();
            pstm2.close();

            JOptionPane.showMessageDialog(null, "Dados excluidos com sucesso");

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO " + e);
        }
    }

    public void ExcluirExame(Exame objExame) {

        String sql = "delete from exame where paciente_idpaciente = ? and nomeimagem = ?;  ";

        conn = new ConexaoDAO().conexaoBD();

        //exclui da pasta
        String nome = objExame.getNomeimagem();

        //deleta a imagem na pasta
        try {
            File imagem = new File("..\\imagens\\" + nome);
            imagem.delete();
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO " + e);
        }

        try {

            pstm = conn.prepareStatement(sql);

            pstm.setInt(1, objExame.getPaciente_idpaciente());
            pstm.setString(2,objExame.getNomeimagem());

            pstm.execute();
            pstm.close();

            JOptionPane.showMessageDialog(null, "Exame excluido.");

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "PacienteDAO " + e);
        }

    }
}
