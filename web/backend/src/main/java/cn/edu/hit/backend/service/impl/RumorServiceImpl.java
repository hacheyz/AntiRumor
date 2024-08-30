package cn.edu.hit.backend.service.impl;

import cn.edu.hit.backend.mapper.RumorMapper;
import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Rumor;
import cn.edu.hit.backend.pojo.Tag;
import cn.edu.hit.backend.service.RumorService;

import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

@Service
public class RumorServiceImpl implements RumorService {
  @Autowired
  private RumorMapper rumorMapper;

  // 分页查询
  @Override
  public PageBean<Rumor> pagelist(Map<String, Object> map) {
    //1.创建PageBean对象
    PageBean<Rumor> pb = new PageBean<>();
    Integer pageNum = (Integer) map.get("pageNum");
    Integer pageSize = (Integer) map.get("pageSize");

    String searchRumor = (String) map.get("searchRumor");
    // 此处的tags是由逗号连接的标签字符串
    String searchTags = (String) map.get("tags");

    List<String> searchTagList = null;
    if(searchTags!=null && !searchTags.trim().isEmpty()) {
      searchTagList = Arrays.asList(searchTags.split(","));
    }

    //2.开启分页查询 PageHelper
    PageHelper.startPage(pageNum, pageSize);

//    System.out.println(searchTags);
//    System.out.println(searchTagList.size());

    //3.调用mapper
    List<Rumor> rumors = rumorMapper.pagelist(searchRumor, searchTagList, searchTagList.size());

    for (Rumor rumor : rumors) {
      List<Tag> tagsForRumor = rumorMapper.getTagsForRumor(rumor.getId());
      String[] temp = new String[tagsForRumor.size()];
      for(int i = 0; i<tagsForRumor.size(); ++i) {
        temp[i] = tagsForRumor.get(i).getName();
      }
//      System.out.println(temp);
      rumor.setTags(temp);
    }

    //Page中提供了方法,可以获取PageHelper分页查询后 得到的总记录条数和当前页数据
    Page<Rumor> p = (Page<Rumor>) rumors;

    //把数据填充到PageBean对象中
    pb.setTotal(p.getTotal());
    pb.setItems(p.getResult());

    return pb;
  }

  @Override
  public List<Tag> getTagsForRumor(Integer rumorId) {
    return rumorMapper.getTagsForRumor(rumorId);
  }

}
