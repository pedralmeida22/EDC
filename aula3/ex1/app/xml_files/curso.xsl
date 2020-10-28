<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="curso">
        <h2><xsl:value-of select="nome"></xsl:value-of></h2>

        <img>
            <xsl:attribute name="src">
                <xsl:value-of select="imagem"></xsl:value-of>
            </xsl:attribute>
        </img>

        <ul>
            <li>Guid: <xsl:value-of select="guid"></xsl:value-of></li>

            <li>Código: <xsl:value-of select="codigo"></xsl:value-of></li>

            <li>Grau: <xsl:value-of select="grau"></xsl:value-of></li>

            <li>Áreas Científicas:
                <ol>
                    <xsl:for-each select="areas/area">
                        <li><xsl:value-of select="."></xsl:value-of></li>
                    </xsl:for-each>
                </ol>
            </li>

            <li>Departamentos:
                <ol>
                    <xsl:for-each select="departamentos/departamento">
                            <li>
                                <a target="_blank">
                                    <xsl:attribute name="href">
                                        <xsl:value-of select="url"/>
                                    </xsl:attribute>
                                    <xsl:value-of select="nome"/>
                                </a>
                            </li>
                    </xsl:for-each>
                </ol>
            </li>

            <li>
                Diretor:
                <ul>
                    <xsl:for-each select="director">
                        <li>Nome: <xsl:value-of select="titulo"></xsl:value-of>&#160;<xsl:value-of select="nome"/></li>
                        <li>Email: <xsl:value-of select="email"/></li>
                    </xsl:for-each>
                </ul>
            </li>

            <li>
                Médias:
                <table border="1px">
                    <tr>
                        <th>Fase 1</th>
                        <th>Fase 3</th>
                        <th>Fase 3</th>
                    </tr>
                    <xsl:for-each select="medias">
                    <tr>
                        <td><xsl:value-of select="fase1"></xsl:value-of></td>
                        <td><xsl:value-of select="fase2"></xsl:value-of></td>
                        <td><xsl:value-of select="fase3"></xsl:value-of></td>
                    </tr>
                    </xsl:for-each>
                </table>
            </li>

            <li>
                Vagas:
                <table border="1px">
                    <tr>
                        <th>Fase 1</th>
                        <th>Fase 3</th>
                        <th>Fase 3</th>
                    </tr>
                    <xsl:for-each select="vagas">
                    <tr>
                        <td><xsl:value-of select="fase1"></xsl:value-of></td>
                        <td><xsl:value-of select="fase2"></xsl:value-of></td>
                        <td><xsl:value-of select="fase3"></xsl:value-of></td>
                    </tr>
                    </xsl:for-each>
                </table>
            </li>

            <li>Regime: <xsl:value-of select="regime"></xsl:value-of></li>

            <li>Propinas: <xsl:value-of select="proprinas"></xsl:value-of></li>

            <li>Duração: <xsl:value-of select="duracao"></xsl:value-of></li>

        </ul>
    </xsl:template>
</xsl:stylesheet>