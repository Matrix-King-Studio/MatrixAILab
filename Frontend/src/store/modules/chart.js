const state = {
    chart: null,
}

const mutations = {
    SetChart: (state, chart) => {
        state.chart = chart
    },
}

const actions = {

}

export default {
    namespaced: true,
    state,
    mutations,
    actions
}