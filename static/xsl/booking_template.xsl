<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html" indent="yes"/>

<xsl:template match="/">
  <html>
    <head>
      <title>Bookings Report</title>
    </head>
    <body>
      <h2>User Bookings</h2>
      <table border="1">
        <tr>
          <th>Car Make</th>
          <th>Car Model</th>
          <th>Car Year</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Transmission Type</th>
          <th>Price</th>
          <th>GPS Service</th>
          <th>Additional Requests</th>
        </tr>
        <xsl:for-each select="bookings/booking">
          <tr>
            <td><xsl:value-of select="carMake"/></td>
            <td><xsl:value-of select="carModel"/></td>
            <td><xsl:value-of select="carYear"/></td>
            <td><xsl:value-of select="startDate"/></td>
            <td><xsl:value-of select="endDate"/></td>
            <td><xsl:value-of select="transmissionType"/></td>
            <td><xsl:value-of select="price"/></td>
            <td><xsl:value-of select="gpsService"/></td>
            <td><xsl:value-of select="additionalRequests"/></td>
          </tr>
        </xsl:for-each>
      </table>
    </body>
  </html>
</xsl:template>

</xsl:stylesheet>
