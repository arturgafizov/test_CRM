console.log('Hello world')


$(function () {
  jGrid()
  getUserList()

});


function getUserList() {
    let table = $('#jsGrid1')


    $.ajax({
      url: table.attr('data-href'),
      type: 'GET',
      success: function (data){
          console.log('success', data)
          renderUserList(data, table)
      },
      error: function (data){
          console.log('error', data)
      }
  })
}

// function Link(id) {
//
//     var row = id.split("=");
//     var row_ID = row[1];
//     var sitename= $("#users_grid").getCell(row_ID, 'Site_Name');
//     var url = "http://"+sitename; // sitename will be like google.com or yahoo.com
//
//     window.open(url);
// }

const jGrid = () => {
      let table = $('#jsGrid1')
      table.jsGrid({
        width: "100%",
        height: "auto",

        autoload:   true,
        paging:     true,
        pageSize:   5,
        pageButtonCount: 5,
        pageIndex:  1,

        sorting: true,


        // controller: {
        //   loadData: function(filter) {
        //     console.log(filter)
        //     return $.ajax({
        //       url: table.attr('data-href'),
        //       dataType: "json",
        //       type: "GET"
        //     });
        //   }
        // },
        // colNames: ['id', 'full_name', 'email', 'balance'],
        // colModel: [
        //             { name: 'id',
        //               index: 'id',
        //               width: 130,
        //               editable: false,
        //               sortable: false,
        //               formatter: 'showlink',
        //               formatoptions: {
        //                 baseLinkUrl: 'javascript:',
        //                 showAction: "Link('",
        //                 addParam: "');"
        //               }
        //             },
        //             { name: 'full_name', index: 'full_name', width: 400, editable: false, sortable: false } ,
        //             { name: 'email', index: 'email', width: 400, editable: false, sortable: false }  ,
        //             { name: 'balance', index: 'balance', width: 400, editable: false, sortable: false }
        // ]
        fields: [
            { name: "id", type: "number", width: 100, height: 150 },
            { name: "full_name", type: "text", width: 150 },
            { name: "email", type: "text", width: 150 },
            { name: "balance", type: "text", width: 100 },
        ]
    });
}

function renderUserList(data, table) {
    table.attr('data-href', data.next)
    let dataTable = $('#jsgrid-table')
    console.log(dataTable)
    dataTable.empty()
    dataTable.append('<tbody id="dataTbody"></tbody>')
    let tbody = $('#dataTbody')
    console.log(data, table)
    $.each(data, function(i){
      console.log(data[i])
      let item = `

      <tr class="jsgrid-cell" style="width: 150px;">
        <td class="jsgrid-cell" style="width: 150px;">${data[i].id} </td
        <td class="jsgrid-cell" style="width: 50px;"><${data[i].full_name}</td>
        <td class="jsgrid-cell" style="width: 200px;">${data[i].email}</td>
        <td class="jsgrid-cell" style="width: 100px;">${data[i].balance}</td>
        <input type="checkbox" disabled=""></td>
      </tr>
        `

    tbody.append(item)
  })

}

