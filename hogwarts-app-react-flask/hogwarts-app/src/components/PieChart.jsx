import React from 'react';
import { Pie } from 'react-chartjs-2';
import { getPieChartData } from '../lib/api'
import { getCoursesPieChartData } from '../lib/api'


export default class PieChart extends React.Component {
    constructor() {
        super();
        this.state = {
            labels: [],
            datasets: [
              {
                // label: 'Rainfall',
                backgroundColor: [
                  '#B21F00',
                  '#C9DE00',
                  '#2FDE00',
                  '#00A6B4',
                  '#6800B4'
                ],
                hoverBackgroundColor: [
                '#501800',
                '#4B5000',
                '#175000',
                '#003350',
                '#35014F'
                ],
                data: []
              }
            ]
          }
      }

componentDidMount(){
    this.fetchData()
}

async fetchData(){
  let res
    if (this.props.skill_type === 'course'){
      res = await getCoursesPieChartData()
    } else {
      res = await getPieChartData(this.props.skill_type)
    }
    let datasets = this.state.datasets
    datasets[0].data = await res.data.data
    this.setState({ datasets})
    this.setState({ labels: await res.data.labels})
}

  render() {
      const { chart_header } = this.props
    return (
      <div>
        <Pie
          data={this.state}
          options={{
            title:{
              display:true,
              text: chart_header,
              fontSize:20
            },
            legend:{
              display:true,
              position:'right'
            }
          }}
        />
      </div>
    );
  }
}