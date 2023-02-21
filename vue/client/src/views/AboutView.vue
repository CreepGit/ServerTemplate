<script lang="ts" setup>
import { ref, onMounted, onUnmounted, type Ref } from 'vue';
import { Chart, LineElement, PointElement, BarController, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Scale, LineController } from 'chart.js'

const ctx: Ref<HTMLCanvasElement|null> = ref(null)
const data = ref([1,2,3,4,10,1])

let chart: Chart|null = null

let dataInterval: number|null = null

const style = getComputedStyle(document.body);
onMounted(()=>{
  if (!ctx.value) return;
  chart = new Chart(ctx.value, {
    type: 'line',
    data: {
      labels: new Array(data.value.length).fill(0),
      datasets: [{
        label: '# of Votes',
        data: data.value,
        borderWidth: 1,
        backgroundColor: 'rgb(0, 189, 126)',
        borderColor: 'rgb(0, 189, 126)',
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          suggestedMin: -10,
          suggestedMax: 10,
        },
        x: {
          ticks: {
            display: false,
          },
        },
      },
    }
  });

  dataInterval = setInterval(() => {
    if (chart == null) return;
    chart.data.datasets.forEach((dataset) => {
      let newData: any[] = dataset.data
      for (let index = 0; index < newData.length; index++) {
        if (Math.random() < 0.7) continue;
        if (Math.random()*100-newData[index]*3 < 50) {
          newData[index] -= 1
        } else {
          newData[index] += 1
        }
      }
      dataset.data = newData;
    });
    chart.update()
  }, 250);
})

onUnmounted(()=>{
  if (dataInterval !== null) {
    clearInterval(dataInterval)
  }
})


Chart.register(BarController, LineController ,BarElement, LineElement, PointElement, CategoryScale, LinearScale)
</script>

<template>
  <div class="about">
    <h1>This is an about page</h1>
    <br>
    <canvas ref="ctx"></canvas>
  </div>
</template>

<style>
</style>
